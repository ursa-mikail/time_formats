#!/bin/bash

# Capture START time
start_epoch=$(date +%s.%N)
start_fmt=$(date +"%Y-%m-%d_%H%M_%S_%3N_%3N_%2N")

# Sleep 5 seconds
sleep 5

# Capture END time
end_epoch=$(date +%s.%N)
end_fmt=$(date +"%Y-%m-%d_%H%M_%S_%3N_%3N_%2N")

# Calculate difference using bc (seconds.nanoseconds)
diff_sec=$(echo "$end_epoch - $start_epoch" | bc -l)

# Split seconds and nanoseconds
start_sec=$(echo "$start_epoch" | cut -d. -f1)
start_nsec=$(echo "$start_epoch" | cut -d. -f2)
end_sec=$(echo "$end_epoch" | cut -d. -f1)
end_nsec=$(echo "$end_epoch" | cut -d. -f2)

# Handle nanosecond underflow
if (( 10#$end_nsec < 10#$start_nsec )); then
  end_sec=$((end_sec - 1))
  end_nsec=$((10#$end_nsec + 1000000000))
fi

delta_sec=$((end_sec - start_sec))
delta_nsec=$((10#$end_nsec - 10#$start_nsec))

# Breakdown nanoseconds to ms/us/ns
ms=$(printf "%03d" $((delta_nsec / 1000000)))
us=$(printf "%03d" $(((delta_nsec / 1000) % 1000)))
ns=$(printf "%02d" $((delta_nsec % 100)))

# Format delta as a pseudo timestamp delta (not an actual date)
delta_fmt=$(printf "0000-00-00_0000_%02d_%s_%s_%s" "$delta_sec" "$ms" "$us" "$ns")

# Print everything
echo "Start Time (formatted): $start_fmt"
echo "End Time   (formatted): $end_fmt"
echo
echo "⏱ Full Range Time Difference:"
echo "-> Human Format Delta: $delta_fmt"
echo "-> Epoch  Format Delta: $diff_sec seconds"

