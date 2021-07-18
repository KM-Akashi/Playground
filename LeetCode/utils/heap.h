#pragma once
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

struct Heap
{
    int *heap;
    int heapSize;
    int maxHeapSize;
    bool reverse;
};

struct Heap *CreateHeap(int maxHeapSize, bool reverse)
{
    struct Heap *heap = (struct Heap *)malloc(sizeof(struct Heap));
    heap->heap = (int *)malloc(sizeof(int) * maxHeapSize);
    heap->heapSize = 0;
    heap->maxHeapSize = maxHeapSize;
    heap->reverse = reverse;
    return heap;
}

void swap(int *a, int *b)
{
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}

void Adjusting(struct Heap *heap)
{
    if (heap->heapSize == 0)
        return;
    for (int i = (heap->heapSize - 1) / 2; i >= 0; i--)
    {
        int lChild = 2 * i + 1;
        int rChild = 2 * i + 2;
        if (heap->reverse)
        {
            if (lChild < heap->heapSize && heap->heap[i] > heap->heap[lChild])
                swap(heap->heap + i, heap->heap + lChild);
            if (rChild < heap->heapSize && heap->heap[i] > heap->heap[rChild])
                swap(heap->heap + i, heap->heap + rChild);
        }
        else
        {
            if (lChild < heap->heapSize && heap->heap[i] < heap->heap[lChild])
                swap(heap->heap + i, heap->heap + lChild);
            if (rChild < heap->heapSize && heap->heap[i] < heap->heap[rChild])
                swap(heap->heap + i, heap->heap + rChild);
        }
    }
}

// Parent   (index-1)/2
// Node     index
// Child    Left 2*index+1 Right 2*index+2
int AddToHeap(struct Heap *heap, int val)
{
    if (heap->heapSize + 1 <= heap->maxHeapSize)
    {
        heap->heap[heap->heapSize] = val;
        heap->heapSize += 1;
        Adjusting(heap);
        return heap->heapSize;
    }
    return -1;
}

int PopFromHeap(struct Heap *heap)
{
    if (heap->heapSize == 0)
        return 0;
    int pop = heap->heap[0];
    swap(heap->heap, heap->heap + heap->heapSize - 1);
    heap->heapSize -= 1;
    Adjusting(heap);
    return pop;
}