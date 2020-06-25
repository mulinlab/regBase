## regBase
   regBase is a comprehensively integrated non-coding regulatory prediction scores and composite prediction models from existing tools for base-wise annotation of human genome. As such, the regBase resource provides convenience to prioritize functional regulatory SNVs and assist the fine mapping of causal regulatory SNVs without queries from numerus sources. 
   
   Inspired by the evident significance of ensemble prediction for pathogenic/deleterious nonsynonymous substitution, regBase also systematically constructs three composite models to score functional, pathogenic and cancer driver non-coding regulatory SNVs. The prediction scores of these models are also intergrated into regBase dataset.
   
   - Please note some component score of regBase contains specific licence or usage constraints for non-academic usage. regBase does not grant the non-academic usage of those scores, so please contact the original score/method providers for proper usage purpose.  
 
   - We welcome any discussion, suggestion and potential contribution of new functional prediction scores through github or contact Dr. Mulin Jun Li (mulinli{at}connect.hku.hk).
   
   - Citation. regBase: whole genome base-wise aggregation and functional prediction for human non-coding regulatory variants. Zhang S, He Y, Liu H, Zhai H, Huang D, Yi X, Dong X, Wang Z, Zhao K, Zhou Y, Wang J, Yao H, Xu H, Yang Z, Sham PC, Chen K, Li MJ*. Nucleic Acids Res. 2019 Dec 2;47(21):e134.

**Updates**
<blockquote>
   - regBase V1.0 is released. Its current version is compiled from 23 different tools on functional annotation of non-coding variants, including Basset, CADD, CATO, CDTS, CScape, DANN, DanQ, DeepSEA, deltaSVM, Eigen, FATHMM-MKL, FATHMM-XF, FIRE, fitCons, FunSeq, FunSeq2, GenoCanyon, GWAS3D, GWAVA, LINSIGHT, ReMM, RSVP, SuRFR and PRVCS. Since some tools only support annotations for 1000 Genome Project variants, or take long runtime to compute functional scores, it first built a database, called <i>regBase Common</i>, which contains functional scores from 23 tools for 38,248,779 in the 1000 Genome Project phase 3. Among these integrated dataset, 13 tools provide precomputed scores for almost all possible substitutions of single nucleotide variant (SNV) in the human reference genome. Therefore, it also constructed a complete base-wise aggregation of non-coding variant functional scores for 8,575,894,770 substitutions of SNV, called <i>regBase</i>.
</blockquote>

<blockquote>
   - regBase V1.1 is released. Five genome-wide functional scores were added, including DVAR, FitCons2, ncER, Orion, PAFA. Now <i>regBase</i> contains 18 tools and <i>regBase Common</i> contains 28 tools.
</blockquote>

## Download
### Dataset Release: V1.1 (without regBase prediction update, hg19) [file](https://drive.google.com/drive/folders/1vd2XR36hiur5QseQcKBHBhd7eGE6YwDd?usp=sharing)

### Dataset Release: V1.0 (hg19) [file](https://drive.google.com/drive/folders/1XU7p3W5Jr6X8ObCoE0dQtLGtcJxLdw0J?usp=sharing)

## Usage
### Score interpretation and prioritization

Similar to CADD C-scores and it's phred-like scores, the raw scores reported by each single tool could be obscure and less-comparable across tools and versions, we recommend to use phred-like scores ("scaled raw scores") for the likely causal variant prioritization and even for comparison among different models (ranging from 1 to 99, and based on the rank of each variant relative to all possible 8.6 billion substitutions in the human reference genome). However, raw scores could be used to evaluate the base-wise differences at specific genomic region or to compare score distributions among different groups of variants, as they preserve distinctions that may be relevant across the entire scoring spectrum (see more guidelines from [CADD information page](https://cadd.gs.washington.edu/info)).

[The Youden's J statistic](https://github.com/mulinlab/regBase/blob/master/trained_model/YoudensJ.txt) for each tool and combined score was released together with our initial models, which could be used to classify positive and negative variants in corresponding models. 

### Basic usage

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
