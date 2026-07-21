# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Pytest file for calling integration bash scripts."""

# @@ If your repo does not require any of its own tiny sectors, delete this file.
# @@ IF your repo DOES require tiny sectors, update any lines containing @@
# @@ within this file appropriately.  Actual sample tests are commented out with #@@
# @@ to ensure tests pass in template_basic_plugin, so uncomment any lines needed for
# @@ testing and evaluating tiny sectors within your repo.

import os
import pytest

# Only use base_setup, because full_setup requires ALL test data repositories.
from tests.integration_tests.test_integration import base_setup  # noqa: F401

from tests.integration_tests.test_integration import (
    run_script_with_bash,
    setup_environment as setup_geoips_environment,
)

global_example_integ_test_calls = [
    ##################################################################################
    # ### Scripts to produce global imagery outputs specifically for diagnostic
    # ### purposes, and identifying day/night/spatial contents of a given dataset.
    # ### More information in geoips/tests/integration_tests/test_tiny_sector_geoips.py
    ##################################################################################
    # @@ Only include datasets here that are specific to this repository, and are not
    # @@ included in other repositories.
    # @@ (
    # @@     "$geoips_repopath/tests/example_scripts/global_terminator_satzen.sh "
    # @@     "@@abi_netcdf@@ "
    # @@     "Test-@@ABI-B14@@ "
    # @@     "@@${GEOIPS_TESTDATA_DIR}/test_data_abi/data/goes17_20210718_0150/*@@"  # noqa: E501
    # @@ ),
    # @@ This is also included in the main geoips repo, but included here for reference.
    # @@ Remove this example for your own repository, add other examples as needed.
    (
        "$GEOIPS/tests/example_scripts/global_terminator_satzen.sh "
        "ahi_hsd "
        "Test-AHI-B13 "
        "$GEOIPS_TESTDATA_DIR/test_data_ahi/data/20200405_0000/HS_H08*"  # noqa: E501
    ),
]

tiny_sector_overlay_integ_test_calls = [
    ##################################################################################
    # ### Output geoips test sector overlays on a global map to identify location of
    # ### each defined tiny sector.  Used for diagnostic purposes to evaluate location
    # ### and size of each tiny sector.
    ##################################################################################
    ##################################################################################
    # ### No satellite-specific test sectors in this repo, as those are included in the
    # ### main geoips repo.
    ##################################################################################
    ##################################################################################
    # ### Dataset specific test sectors, reliant on specific time of day and/or
    # ### meteorological features within the dataset.
    ##################################################################################
    # @@ "geoips test sector --overlay @@test_goes17_eqc_10km_terminator_20210718T0150Z@@ -o $GEOIPS_OUTDIRS/example_test_imagery_outputs ",  # noqa: E501
    # @@ Ensure you include any tiny sector that is created/defined in this repository.
    "geoips test sector --overlay template_test_himawari8_eqc_10km_terminator_20200405T0000Z -o $GEOIPS_OUTDIRS/example_test_imagery_outputs ",  # noqa: E501
]


tiny_sector_integ_test_calls = [
    ##################################################################################
    # ### Test the actual output of each specified tiny sector defined within this repo.
    # ### tiny_sectors_geostationary.sh is a wrapper test script to produce the
    # ### specified tiny sector output, and compare it with the stored comparison
    # ### output imagery.
    # ### More information in geoips/tests/integration_tests/test_tiny_sector_geoips.py
    ##################################################################################
    ##################################################################################
    # ### No satellite-specific test sectors in this repo, as those are included in the
    # ### main geoips repo.
    ##################################################################################
    ##################################################################################
    # ### Dataset specific test sectors, reliant on specific time of day and/or
    # ### meteorological features within the dataset.
    ##################################################################################
    # @@ (
    # @@     "$geoips_repopath/tests/integration_tests/tiny_sectors/tiny_sectors_geostationary.sh "  # noqa: E501
    # @@     "@@test_goes17_eqc_10km_terminator_20210718T0150Z@@ "
    # @@     "@@abi_netcdf@@ "
    # @@     "Test-@@ABI-B14-Night@@-Only "
    # @@     "@@repo_name@@ "
    # @@     "@@$GEOIPS_TESTDATA_DIR/test_data_abi/data/goes17_20210718_0150/*@@"  # noqa: E501
    # @@ ),
    # @@ Ensure you include any tiny sector that is created/defined in this repository.
    (
        "$geoips_repopath/tests/integration_tests/tiny_sectors/tiny_sectors_geostationary.sh "  # noqa: E501
        "template_test_himawari8_eqc_10km_terminator_20200405T0000Z "
        "ahi_hsd "
        "Test-AHI-B13-Day-Only "
        "template_basic_plugin "
        "$GEOIPS_TESTDATA_DIR/test_data_ahi/data/20200405_0000/*"
    ),
]


def setup_environment():
    """
    Set up necessary environment variables for integration tests.

    Configures paths and package names for the GeoIPS core and its plugins by
    setting environment variables required for the integration tests. Assumes
    that 'GEOIPS_PACKAGES_DIR' is already set in the environment.

    Notes
    -----
    The following environment variables are set:
    - geoips_repopath
    - geoips_pkgname
    - repopath
    - pkgname
    """
    # Setup base geoips environment
    setup_geoips_environment()
    # Setup current repo's environment
    os.environ["repopath"] = os.path.realpath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
    os.environ["pkgname"] = "@@my_package@@"


@pytest.mark.optional
@pytest.mark.sample_output
@pytest.mark.sector_evaluation
@pytest.mark.sector_global_example
@pytest.mark.parametrize("script", global_example_integ_test_calls)
def test_integ_global_example_script(base_setup: None, script: str):  # noqa: F811
    """
    Run integration test scripts by executing specified shell commands.

    Parameters
    ----------
    script : str
        Shell command to execute as part of the integration test. The command may
        contain environment variables which will be expanded before execution.

    Raises
    ------
    subprocess.CalledProcessError
        If the shell command returns a non-zero exit status.
    """
    setup_environment()
    run_script_with_bash(script)


@pytest.mark.optional
@pytest.mark.sample_output
@pytest.mark.sector_evaluation
@pytest.mark.sector_overlay
@pytest.mark.parametrize("script", tiny_sector_overlay_integ_test_calls)
def test_integ_tiny_sector_overlay_script(base_setup: None, script: str):  # noqa: F811
    """
    Run integration test scripts by executing specified shell commands.

    Parameters
    ----------
    script : str
        Shell command to execute as part of the integration test. The command may
        contain environment variables which will be expanded before execution.

    Raises
    ------
    subprocess.CalledProcessError
        If the shell command returns a non-zero exit status.
    """
    setup_environment()
    run_script_with_bash(script)


@pytest.mark.integration
@pytest.mark.sector_evaluation
@pytest.mark.sector_output_comparison
@pytest.mark.parametrize("script", tiny_sector_integ_test_calls)
def test_integ_tiny_sector_script(base_setup: None, script: str):  # noqa: F811
    """
    Run integration test scripts by executing specified shell commands.

    Parameters
    ----------
    script : str
        Shell command to execute as part of the integration test. The command may
        contain environment variables which will be expanded before execution.

    Raises
    ------
    subprocess.CalledProcessError
        If the shell command returns a non-zero exit status.
    """
    setup_environment()
    run_script_with_bash(script)
