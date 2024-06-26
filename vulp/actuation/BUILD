# -*- python -*-
#
# Copyright 2022 Stéphane Caron

load("//tools/lint:lint.bzl", "add_lint_tests")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "imu_data",
    hdrs = [
        "ImuData.h",
    ],
    deps = [
        "@eigen",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "servo_layout",
    hdrs = [
        "ServoLayout.h",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "resolution",
    hdrs = [
        "resolution.h",
    ],
    deps = [
        "//vulp/actuation/moteus",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "interface",
    hdrs = [
        "default_action.h",
        "Interface.h",
    ],
    srcs = [
        "Interface.cpp",
    ],
    deps = [
        "//vulp/actuation/moteus",
        ":imu_data",
        ":resolution",
        ":servo_layout",
        "@palimpsest",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "mock_interface",
    hdrs = [
        "MockInterface.h",
    ],
    srcs = [
        "MockInterface.cpp",
    ],
    deps = [
        "//vulp/actuation:interface",
        "//vulp/utils:synchronous_clock",
        "@eigen",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "bullet_utils",
    hdrs = [
        "BulletImuData.h",
        "bullet_utils.h",
    ],
    deps = [
        ":imu_data",
        "@bullet",
        "@eigen",
        "@palimpsest",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "bullet_interface",
    hdrs = [
        "BulletContactData.h",
        "BulletImuData.h",
        "BulletInterface.h",
        "BulletJointProperties.h",
        "bullet_utils.h",
    ],
    srcs = [
        "BulletInterface.cpp",
    ],
    data = [
        "//vulp/actuation/bullet/plane",
    ],
    deps = [
        "//vulp/actuation:interface",
        "//vulp/utils:synchronous_clock",
        "@bazel_tools//tools/cpp/runfiles",
        "@bullet",
        "@eigen",
        "@palimpsest",
    ],
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "pi3hat_interface",
    hdrs = [
        "Pi3HatInterface.h",
    ],
    srcs = select({
        "//:pi64_config": ["Pi3HatInterface.cpp"],
        "//conditions:default": [],
    }),
    deps = [
        "//vulp/utils:realtime",
        ":interface",
    ] + select({
        "//:pi64_config": [
            "@org_llvm_libcxx//:libcxx",
            "@pi3hat//lib/cpp/mjbots/pi3hat:libpi3hat",
        ],
        "//conditions:default": [],
    }),
    include_prefix = "vulp/actuation",
)

cc_library(
    name = "actuation",
    deps = [
        ":bullet_interface",
        ":mock_interface",
    ] + select({
        "//:pi64_config": [":pi3hat_interface"],
        "//conditions:default": [],
    }),
    include_prefix = "vulp/actuation",
)

add_lint_tests()
