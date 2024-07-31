# CPU profiling with `cProfile`

Profile CPU usage, the stats printed include the different functions called, the number of times they were called
and the time spent.

```python
def main():
    ...

if __name__ == "__main__":
    import cProfile
    import pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    # Use sort_stats(pstats.SortKey.CALLS) to sort by number of calls
    stats = pstats.Stats(profiler).strip_dirs().sort_stats('cumulative')
    stats.print_stats()
```