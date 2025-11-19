install:
	uv sync

VD-games:
	uv run VD-games

VD-calc:
	uv run VD-calc
VD-gcd:
	VD-gcd
VD-progression:
	uv run VD-progression

VD-prime:
	uv run VD-prime
build:
	uv build

package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check VD-games
