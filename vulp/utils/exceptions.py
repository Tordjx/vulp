#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2023 Inria


class VulpException(Exception):
    """Base class for exceptions raised by Vulp."""


class PerformanceException(VulpException):
    """Exception raised when a performance issue is detected."""
