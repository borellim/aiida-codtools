# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from aiida_codtools.calculations.cif_base import CifBaseCalculation


class CifSplitPrimitiveCalculation(CifBaseCalculation):
    """CalcJob plugin for the `cif_split_primitive` script of the `cod-tools` package."""

    _default_parser = 'codtools.cif_split_primitive'
    _directory_split = 'split'

    def prepare_for_submission(self, folder):
        calcinfo = super(CifSplitPrimitiveCalculation, self).prepare_for_submission(folder)

        split_dir = folder.get_abs_path(self._directory_split)
        os.mkdir(split_dir)

        calcinfo.codes_info[0].cmdline_params.extend(['--output-dir', self._directory_split])
        calcinfo.retrieve_list.append(self._directory_split)

        return calcinfo
