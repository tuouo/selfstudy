#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge(default, override):
    r = {}
    for k, v in default.items():
        r[k] = (merge(v, override[k]) if isinstance(v, dict) else override[k]) if k in override else v
    return r

import config_default
configs = config_default.configs
try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass    # if no config_override.py

import DictSupportPoint as Dict
configs = Dict.toDict(configs)