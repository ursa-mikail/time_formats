package main

import (
	"fmt"
	"time"
)

func formatTimestamp(t time.Time) string {
	return fmt.Sprintf("%04d-%02d-%02d_%02d%02d_%02d_%03d_%03d_%02d",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second(),
		t.Nanosecond()/1e6,      // milliseconds
		(t.Nanosecond()/1e3)%1e3, // microseconds
		(t.Nanosecond()/1e1)%1e2, // last 2 digits of nanoseconds
	)
}

func main() {
	start := time.Now()
	startFmt := formatTimestamp(start)

	time.Sleep(5 * time.Second)

	end := time.Now()
	endFmt := formatTimestamp(end)

	duration := end.Sub(start)
	seconds := duration.Seconds()
	nanos := duration.Nanoseconds()

	ms := (nanos / 1e6)
	us := (nanos / 1e3) % 1000
	ns := (nanos / 1e1) % 100

	fmt.Println("Start time formatted :", startFmt)
	fmt.Println("End time formatted   :", endFmt)
	fmt.Println()

	fmt.Printf("⏱ Full Range Time Difference:\n")
	fmt.Printf("-> Human Format Delta : 0000-00-00_0000_%02d_%03d_%03d_%02d\n",
		int(duration.Seconds()), ms%1000, us, ns)
	fmt.Printf("-> Epoch Format Delta : %.9f seconds\n", seconds)
}


/*
go mod tidy
go run time_diff.go

// build it as a standalone binary:
go build -o time_diff_go time_diff.go
./time_diff_go

*/