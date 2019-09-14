## regBase
   regBase is a comprehensively integrated non-coding regulatory prediction scores and composite prediction models from existing tools for base-wise annotation of human genome. As such, the regBase resource provides convenience to prioritize functional regulatory SNVs and assist the fine mapping of causal regulatory SNVs without queries from numerus sources. 
   
   Inspired by the evident significance of ensemble prediction for pathogenic/deleterious nonsynonymous substitution, regBase also systematically constructs three composite models to score functional, pathogenic and cancer driver non-coding regulatory SNVs. The prediction scores of these models are also intergrated into regBase dataset.
   
   - Please note some component score of regBase contains specific licence or usage constraints for non-academic usage. regBase does not grant the non-academic usage of those scores, so please contact the original score/method providers for proper usage purpose.  
 
   - We welcome any discussion, suggestion and potential contribution of new functional prediction scores through github or contact Dr. Mulin Jun Li (mulinli{at}connect.hku.hk). 

**Updates**
<blockquote>
   - regBase V1.0 is released. Its current version is compiled from 23 different tools on functional annotation of non-coding variants, including Basset, CADD, CATO, CDTS, CScape, DANN, DanQ, DeepSEA, deltaSVM, Eigen, FATHMM-MKL, FATHMM-XF, FIRE, fitCons, FunSeq, FunSeq2, GenoCanyon, GWAS3D, GWAVA, LINSIGHT, ReMM, RSVP and SuRFR. Since some tools only support annotations for 1000 Genome Project variants, or take long runtime to compute functional scores, it first built a database, called <i>regBase Common</i>, which contains functional scores from 23 tools for 38,248,779 in the 1000 Genome Project phase 3. Among these integrated dataset, 13 tools provide precomputed scores for almost all possible substitutions of single nucleotide variant (SNV) in the human reference genome. Therefore, it also constructed a complete base-wise aggregation of non-coding variant functional scores for 8,575,894,770 substitutions of SNV, called <i>regBase</i>.
</blockquote>

<blockquote>
   - regBase V1.1 is released. Five genome-wide functional scores were added, including DVAR, FitCons2, ncER, Orion, PAFA. Now <i>regBase</i> contains 18 tools and <i>regBase Common</i> contains 28 tools.
</blockquote>

## Download
### Dataset Release: V1.1 (without regBase prediction update, hg19)

| Description         | Link (Size)                                                  | Tabix Index (Size)                                           |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| regBase             | [file (596G)](http://202.113.53.226/regbase/hg19/v1.1/regBase/regBase_v1.1.gz)      | [tabix index (2.7M)](http://202.113.53.226/regbase/hg19/v1.1/regBase/regBase_v1.1.gz.tbi) |
| regBase Common      | [file (7.7G)](http://202.113.53.226/regbase/hg19/v1.1/regBase_Common/regBase_Common_v1.1.gz) | [tabix index (2.5M)](http://202.113.53.226/regbase/hg19/v1.1/regBase_Common/regBase_Common_v1.1.gz.tbi) |
| MD5Sums             | [file](http://202.113.53.226/regbase/hg19/v1.1/MD5SUMs) |  |

### Dataset Release: V1.0 (hg19)

| Description         | Link (Size)                                                  | Tabix Index (Size)                                           |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| regBase             | [file (541G)](http://202.113.53.226/regbase/hg19/v1.0/regBase/regBase.gz)      | [tabix index (2.7M)](http://202.113.53.226/regbase/hg19/v1.0/regBase/regBase.gz.tbi) |
| regBase Prediction REG/PAT/CAN | [file (233G)](http://202.113.53.226/regbase/hg19/v1.0/regBase/regBase_prediction.gz) | [tabix index (2.7M)](http://202.113.53.226/regbase/hg19/v1.0/regBase/regBase_prediction.gz.tbi) |
| regBase Common      | [file (6.8G)](http://202.113.53.226/regbase/hg19/v1.0/regBase_Common/regBase_Common.gz) | [tabix index (2.5M)](http://202.113.53.226/regbase/hg19/v1.0/regBase_Common/regBase_Common.gz.tbi) |
| regBase Common Prediction | [file (557M)](http://202.113.53.226/regbase/hg19/v1.0/regBase_Common/regBase_Common_prediction.gz) | [tabix index (1.7M)](http://202.113.53.226/regbase/hg19/v1.0/regBase_Common/regBase_Common_prediction.gz.tbi) |
| MD5Sums             | [file](http://202.113.53.226/regbase/hg19/v1.0/MD5SUMs) |  |

### Basic Usage

   Get the CADD prediction scores from regBase (e.g chr10:101388218)
   ```bash
   tabix -p bed regBase.gz 10:101388218-101388218 | cut -f 1-5,6
   ```
   Get the CADD PHRED-score from regBase (e.g chr10:101388218)
   ```bash
   tabix -p bed regBase.gz 10:101388218-101388218 | cut -f 1-5,7
   ```
   Get the regBase_CAN prediction from regBase Prediction (e.g chr10:101388218)
   ```bash
   tabix -p bed regBase_prediction.gz 10:101388218-101388218 | cut -f 1-5,8,9
   ```


## Building regBase models
### Requirements
- python 3.5
- scikit-learn >= 0.20.1
- xgboost >= 0.71
- tabix >= 1.6

### Procedures
If you have everything installed, you can use the best parmeters to train a model as follows:
   ```bash
   cd ./script
   python train_model.py
   ```
If you do not want to train a model from scratch instead of only prediction, you need provide a query file to do it.
   ```bash
   cd ./script
   python regBase_predict.py query_file.bed
   python regBase_Common_predict.py query_file.bed
   ```
The query file must be a list of variants that use the format as:
   ```bash
   ./script/query_file.bed
   ```

## Copyright
Copyright (c) Mulinlab@Tianjin Medical University 2016-2019. All rights reserved.
Please note some component score of regBase contains specific licence or usage constraints for non-academic usage. regBase does not grant the non-academic usage of those scores, so please contact the original score/method providers for proper usage purpose.
