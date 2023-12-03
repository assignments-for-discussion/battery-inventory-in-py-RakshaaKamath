def count_batteries_by_health(present_capacities):
  counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for cap in present_capacities:
    soh = 100.0 * cap / 120.0
    if soh > 80.0:
      counts["healthy"] += 1
    elif soh > 62.0:
      counts["exchange"] += 1
    else:
      counts["failed"] += 1
  print(f"Healthy batteries: {counts['healthy']}\nExchange batteries: {counts['exchange']}\nFailed batteries: {counts['failed']}")
  return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
