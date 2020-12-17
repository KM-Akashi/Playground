package main

import (
	"fmt"
	"time"

	"github.com/jmcvetta/randutil"
)

var (
	sign = make(chan bool)
)

type Node struct {
	Alpha int
	End   bool
	Next  map[*Node]int
}

func NewNode(end bool) *Node {
	return &Node{1, end, make(map[*Node]int)}
}

type Ant struct {
	Delta int
	Tabu  map[*Node]bool
}

func NewAnt() *Ant {
	return &Ant{1, make(map[*Node]bool)}
}

func (a *Ant) SetAlpha() {
	for key := range a.Tabu {
		key.Alpha += a.Delta
	}
	sign <- true
}

func (a *Ant) Run(root *Node) {
	node := root
	if node.End {
		a.Tabu[node] = true
		a.SetAlpha()
		return
	}

	a.Tabu[node] = true

	choices := make([]randutil.Choice, 0, 2)
	for key := range node.Next {
		if _, ok := a.Tabu[key]; !ok {
			choices = append(choices, randutil.Choice{key.Alpha, key})
		}
	}
	if len(choices) == 0 {
		a.SetAlpha()
		return
	}
	result, _ := randutil.WeightedChoice(choices)

	nextNode := result.Item.(*Node)
	time.Sleep(time.Duration(node.Next[nextNode]) * time.Second)
	a.Run(nextNode)
}

func main() {
	ANT_NUMBER := 100

	nodeA := NewNode(false)

	nodeB := NewNode(false)
	nodeC := NewNode(false)
	nodeA.Next[nodeB] = 1
	nodeA.Next[nodeC] = 10

	nodeD := NewNode(false)
	nodeE := NewNode(false)
	nodeB.Next[nodeD] = 10
	nodeB.Next[nodeE] = 1
	nodeC.Next[nodeD] = 10
	nodeC.Next[nodeE] = 10

	nodeF := NewNode(true)
	nodeD.Next[nodeF] = 10
	nodeE.Next[nodeF] = 1

	ants := make([]*Ant, 0)
	for i := 0; i < ANT_NUMBER; i++ {
		ants = append(ants, NewAnt())
	}
	fmt.Println("##### START #####")
	for _, ant := range ants {
		go ant.Run(nodeA)
	}
	for i := 0; i < ANT_NUMBER; i++ {
		<-sign
	}
	fmt.Println("###### END ######")

	fmt.Println("A", nodeA.Alpha)
	fmt.Println("B", nodeB.Alpha, "C", nodeC.Alpha)
	fmt.Println("D", nodeD.Alpha, "E", nodeE.Alpha)
	fmt.Println("F", nodeF.Alpha)
}
