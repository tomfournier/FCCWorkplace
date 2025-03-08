# FCCWorkplace
FCC workplace
## Installation of Software

- [FCCWorkplace](https://github.com/Ang-Li-93/FCCWorkplace)

I am in the process of simplifing these two repos.

Follow the instructions step-by-step.

### Clone the repository

```shell=
git clone git@github.com:Ang-Li-93/FCCWorkplace.git
```
### Install FCCAnalyses
```shell=
cd FCCAnalyses
source /cvmfs/sw.hsf.org/key4hep/setup.sh -r 2024-03-10
source ./setup.sh
fccanalysis build -j 8
cd ..
```

### Install Combine
```shell=
cd HiggsAnalysis-CombinedLimit/
source env_standalone.sh
make -j ${nproc}
cd ../
```

### Install local python packages (i.e. sklearn, xgboost)
```shell=
sh install_venv.sh
source setup_local.sh
```

## Setup After Each Login

1. Navigate to the `FCCAnalysis` repository and run `source setup.sh`.
2. Navigate to `FCCeePhysicsPerformance/case-studies/higgs/dataframe/` and run `source localSetup.sh`.
3. Go to the working directory (`mH-recoil`) and run `source setup.sh`.

**Note:** The working directory is `FCCeePhysicsPerformance/case-studies/higgs/mH-recoil`.

[Note](https://codimd.web.cern.ch/v-2loZ2BSmSurcYI1v-Nkg?both)