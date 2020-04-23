# -*- coding: utf-8 -*-
# Copyright 2007-2020 The HyperSpy developers
#
# This file is part of  HyperSpy.
#
#  HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  HyperSpy.  If not, see <http://www.gnu.org/licenses/>.

"""
Import sklearn.* and randomized_svd from scikit-learn
"""

import warnings


try:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        import sklearn
        import sklearn.decomposition
        from sklearn.utils.extmath import randomized_svd
        from sklearn.exceptions import ConvergenceWarning

        sklearn_installed = True

except ImportError:
    randomized_svd = None
    sklearn_installed = False
