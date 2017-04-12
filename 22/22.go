package main

import (
  "io/ioutil"
  "sort"
  "strings"
  "unicode"
)

func main() {
  names := get_name_list("names.txt")
  println(score_list(names))
}

func get_name_list(filename string) (names []string) {
  dat, err := ioutil.ReadFile(filename)
  check(err)
  var name_list = strings.Split(string(dat), ",")
  for i, name := range name_list {
    name_list[i] = name[1:len(name)-1]
  }
  return name_list
}

func score(name string) (score int) {
  name = strings.ToUpper(name)
  score = 0
  for _, char := range name {
    if unicode.IsUpper(char) {
      alph_pos := int(char) - 64
      score += alph_pos
    }
  }
  return score
}

func score_list(name_list []string) (total_score int) {
  sort.Strings(name_list)
  total_score = 0
  for i, name := range name_list {
    name_score := score(name) * (i + 1)
    total_score += name_score
  }
  return total_score
}

func check(e error) {
  if e != nil {
    panic(e)
  }
}
