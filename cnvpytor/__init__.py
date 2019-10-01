"""
CNVpytor
========
CNVpytor is a Python package and command line tool for CNV analysis
from depth-of-coverage by mapped reads developed in Abyzov Lab, Mayo Clinic.

Documentation::
    https://abyzovlab.github.io/CNVpytor/

Source::
    https://github.com/abyzovlab/CNVpytor

Bug reports::
    https://github.com/abyzovlab/CNVpytor/issues

Install
-------
```
> git clone https://github.com/abyzovlab/CNVpytor.git
> cd CNVpytor
> python setup.py install
```
For single user (without admin privileges) use:
```
> python setup.py install --user
```

## Simple example

Call CNV using read depth:
```
> cnvpytor -root file.pytor -rd file.bam
> cnvpytor -root file.pytor -his 1000 10000 100000
> TODO: cnvpytor -root file.pytor -partition 1000 10000 100000
> TODO: cnvpytor -root file.pytor -call 1000 10000 100000
```

Call CNV using single nucleotide polymorphism::
```
> cnvpytor -root file.pytor -snp file.vcf
> cnvpytor -root file.pytor -pileup file.bam
> TODO: cnvpytor -root file.pytor -baf 10000 100000
> TODO: cnvpytor -root file.pytor -call baf 10000 100000
```

Plot
```
> cnvpytor -root file.pytor -plot stat
> cnvpytor -root file.pytor -plot 10000 100000
> cnvpytor -root file.pytor -plot stat manhattan 100000 -o file.pdf
> cnvpytor -root file.pytor -plot baf -chrom 1 2 3 4
> TODO: cnvpytor -root file.pytor -plot circular
> TODO: cnvpytor -root file.pytor -plot regions 1:10M-20M;2:20M-43M,3:10M-20M
```

## Bugs

Please report any bugs that you find on GitHub:
https://github.com/abyzovlab/CNVpytor/issues

Or, even better, fork the repository on GitHub and create a pull request.

## License

Released under MIT licence.

"""
from __future__ import absolute_import, print_function, division
from .io import *
from .bam import *
from .utils import *
from .fasta import *
from .vcf import *
from .root import *
from .viewer import *

__version__ = '1.0a1'