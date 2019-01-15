#!/usr/bin/env python
# Copyright (C) 2019 by Mulinlab@Tianjin Medical University 2018
# Contact:  Dr. Mulin Jun Li (mulinli{at}connect.hku.hk)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
"""
import optparse, sys
import io, subprocess
import pandas as pd
from sklearn.externals import joblib

# regBase database:
DEFAULT_regBase = '../dataset_V1/regBase/regBase.gz'


def read_bed(x, **kwargs):
    return pd.read_csv(x, sep=r'\s+', header=None, index_col=False, **kwargs)


def regBase_pytabix(arguments, fp):
    cmdline = f'tabix -p bed {arguments} | cut -f 1-5,6,8,10,12,14,16,18,20,22,24,26,28,30,32'
    p = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
    stdout, _ = p.communicate()

    feature = read_bed(io.StringIO(stdout.decode('utf-8'))).set_index(0)
    feature = feature.values[:, :]

    feature_ref = feature[:, 2]
    feature_alt = feature[:, 3]
    rows = feature.shape[0]
    cols = feature.shape[1]


    for ith_row in range(0, rows):
        if feature_ref[ith_row] == ref and feature_alt[ith_row] == alt:
            out_str = str(chr_id) + "\t" + str(position) + "\t" + str(ref) + "\t" + str(alt)
            for ith_dim in range(4, cols):
                out_str = out_str + "\t" + str(feature[ith_row, ith_dim])
            fp.write(out_str+'\n')
        else:
            continue

USAGE = """%prog query-file [options]

The query file must be a list of queries that use the following format:

chromosome,position,reference,Alts

Example:

1,69094,G,A
11,168961,T,A
18,119888,G,A"""

# Establish command-line options:
parser = optparse.OptionParser(usage=USAGE)
parser.add_option('-r', dest='regBase',     default=DEFAULT_regBase,     help='regBase database [default: %default]')
parser.add_option('-o', dest='output_folder',  default='./',                  help='Output file [default: current folder]')
opts, args = parser.parse_args(sys.argv[1:])

# query file
MIN_ARGS = 1
if len(args) != MIN_ARGS :
    parser.print_help()
    sys.exit(1)

queryFile = args[0]


with open(queryFile, 'r') as fp:
    with open('./tmp.bed', 'w') as tmp_fp:
        for line in fp:
            line = line.replace('\n', '')
            line = line.split(',')

            chr_id = line[0]
            position = line[1]
            ref = line[2]
            alt = line[3]

            cmdline = f"{DEFAULT_regBase} {chr_id}:{position}-{position}"
            regBase_pytabix(cmdline, tmp_fp)

# predict regBase REG/CAN/PAT
ds = pd.read_csv('./tmp.bed', header=None, na_values=['.'], sep="\t")
ds_values = ds.values[:, :]
ds_site_info = ds_values[:, 0:3+1]
ds_feature = ds_values[:, 4:]


#------------------------
model_name_set = {'regBase_CAN', 'regBase_PAT', 'regBase_REG'}
model = {}
for model_name in model_name_set:
    # load model from file
    model[model_name] = joblib.load(f'../trained_model/{model_name}.model')

score = {}
out_file = {}
for model_name in model_name_set:
    score[model_name] = model[model_name].predict_proba(ds_feature)[:, -1]
    out_file[model_name] = open(f'{opts.output_folder}/{model_name}.txt', 'w')

for ith_sample in range(0, ds_site_info.shape[0]):
    ith_site_info = ds_site_info[ith_sample, :]

    out_str = str(ith_site_info[0]) + "\t" + str(ith_site_info[1]) + "\t" + str(ith_site_info[2]) + "\t" + str(ith_site_info[3]) + "\t"

    out_str_CAN = out_str + str(score['regBase_CAN'][ith_sample]) + "\n"
    out_str_PAT = out_str + str(score['regBase_PAT'][ith_sample]) + "\n"
    out_str_REG = out_str + str(score['regBase_REG'][ith_sample]) + "\n"

    out_file['regBase_CAN'].write(out_str_CAN)
    out_file['regBase_PAT'].write(out_str_PAT)
    out_file['regBase_REG'].write(out_str_REG)

out_file['regBase_CAN'].close()
out_file['regBase_PAT'].close()
out_file['regBase_REG'].close()

subprocess.check_call([f"rm ./tmp.bed"], shell=True)






