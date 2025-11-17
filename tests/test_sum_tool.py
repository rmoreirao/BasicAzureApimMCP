"""Tests for the sum tool."""

import pytest

from basic_mcp.tools.sum_tool import _sum_impl as sum


class TestSumTool:
    """Test cases for the sum tool."""

    def test_sum_positive_integers(self) -> None:
        """Test sum with positive integers."""
        assert sum(2, 3) == 5.0

    def test_sum_positive_floats(self) -> None:
        """Test sum with positive floats."""
        assert sum(2.5, 3.7) == 6.2

    def test_sum_negative_numbers(self) -> None:
        """Test sum with negative numbers."""
        assert sum(-5, 10) == 5.0
        assert sum(-5, -3) == -8.0
        assert sum(5, -3) == 2.0

    def test_sum_with_zero(self) -> None:
        """Test sum with zero values."""
        assert sum(0, 0) == 0.0
        assert sum(5, 0) == 5.0
        assert sum(0, 5) == 5.0

    def test_sum_very_large_numbers(self) -> None:
        """Test sum with very large numbers."""
        result = sum(1e308, 1e308)
        assert result == 2e308

    def test_sum_mixed_int_float(self) -> None:
        """Test sum with mixed int and float inputs."""
        assert sum(2, 3.5) == 5.5
        assert sum(2.5, 3) == 5.5

    def test_sum_returns_float(self) -> None:
        """Test that sum always returns a float."""
        result = sum(2, 3)
        assert isinstance(result, float)

    def test_sum_invalid_string_input(self) -> None:
        """Test that string inputs raise ValueError."""
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum("2", 3)  # type: ignore
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum(2, "3")  # type: ignore

    def test_sum_invalid_none_input(self) -> None:
        """Test that None inputs raise ValueError."""
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum(None, 3)  # type: ignore
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum(2, None)  # type: ignore

    def test_sum_invalid_bool_input(self) -> None:
        """Test that boolean inputs raise ValueError."""
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum(True, 3)  # type: ignore
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum(2, False)  # type: ignore

    def test_sum_invalid_list_input(self) -> None:
        """Test that list inputs raise ValueError."""
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum([1, 2], 3)  # type: ignore

    def test_sum_invalid_dict_input(self) -> None:
        """Test that dict inputs raise ValueError."""
        with pytest.raises(ValueError, match="must be a numeric type"):
            sum({"a": 1}, 3)  # type: ignore

    def test_sum_edge_case_very_small_numbers(self) -> None:
        """Test sum with very small numbers."""
        assert sum(1e-308, 1e-308) == 2e-308

    def test_sum_precision(self) -> None:
        """Test that sum maintains reasonable precision."""
        result = sum(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10  # Account for floating point precision
