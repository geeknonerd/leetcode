package utils

import (
	"fmt"
	"log"
	"strings"
)

func Assert(x interface{}, y interface{}) {
	if strings.Compare(fmt.Sprintf("%v", x), fmt.Sprintf("%v", y)) != 0 {
		log.Fatalf("assert err: %v != %v\n", x, y)
	} else {
		log.Println("assert ok")
	}
}
