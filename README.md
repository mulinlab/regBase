## regBase
   regBase is a comprehensively integrated non-coding regulatory prediction scores and composite prediction models from existing tools for base-wise annotation of human genome. As such, the regBase resource provides convenience to prioritize functional regulatory SNVs and assist the fine mapping of causal regulatory SNVs without queries from numerus sources. 
   
  Its current version is compiled from 23 different tools on functional annotation of non-coding variants, including Basset, CADD, CATO, CDTS, CScape, DANN, DanQ, DeepSEA, deltaSVM, Eigen, FATHMM-MKL, FATHMM-XF, FIRE, fitCons, FunSeq, FunSeq2, GenoCanyon, GWAS3D, GWAVA, LINSIGHT, ReMM, RSVP and SuRFR. Since some tools only support annotations for 1000 Genome Project variants, or take long runtime to compute functional scores, it first built a database, called **regBase Common**, which contains functional scores from 23 tools for 38,248,779 in the 1000 Genome Project phase 3. Among these integrated dataset, 13 tools provide precomputed scores for almost all possible substitutions of single nucleotide variant (SNV) in the human reference genome. Therefore, it also constructed a complete base-wise aggregation of non-coding variant functional scores for 8,575,894,770 substitutions of SNV, called **regBase**.
   
   Inspired by the evident significance of ensemble prediction for pathogenic/deleterious nonsynonymous substitution, regBase also systematically constructs three composite models to score functional, pathogenic and cancer driver non-coding regulatory SNVs. The prediction scores of these models are also intergrated into rebBase dataset.
   
   - Please note some component score of regBase contains specific licence or usage constraints for non-academic usage. regBase does not grant the non-academic usage of those scores, so please contact the original score/method providers for proper usage purpose.  
 
   - We welcome any discussion, suggestion and potential contribution of new functional prediction scores through github or contact Dr. Mulin Jun Li (mulinli{at}connect.hku.hk). 
   
## Download
**Dataset Release:** V1.0

| Description         | Link (Size)                                                  | Tabix Index (Size)                                           |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| regBase             | [file (541G)](http://mulinlab.org/regbase/hg19/v1.0/regBase/regBase.gz)      | [tabix index (2.7M)](http://mulinlab.org/regbase/hg19/v1.0/regBase/regBase.gz.tbi) |
| regBase Prediction REG/PAT/CAN | [file (233G)](http://mulinlab.org/regbase/hg19/v1.0/regBase/regBase_prediction.gz) | [tabix index (2.7M)](http://mulinlab.org/regbase/hg19/v1.0/regBase/regBase_prediction.gz.tbi) |
| regBase Common      | [file (6.8G)](http://mulinlab.org/regbase/hg19/v1.0/regBase_Common/regBase_Common.bgz) | [tabix index (2.5M)](http://mulinlab.org/regbase/hg19/v1.0/regBase_Common/regBase_Common.bgz.tbi) |
| regBase Common Prediction | [file (557M)](http://mulinlab.org/regbase/hg19/v1.0/regBase_Common/regBase_Common_prediction.bgz) | [tabix index (1.7M)](http://mulinlab.org/regbase/hg19/v1.0/regBase_Common/regBase_Common_prediction.bgz.tbi) |

## Building regBase models
### Requirements
- tabix 1.6
- python 3.5
- scikit-learn 0.18
- pandas 
- numpy
- xgboost > 0.71

