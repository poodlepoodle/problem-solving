class Heap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(A, B) {
    [this.heap[A], this.heap[B]] = [this.heap[B], this.heap[A]];
  }

  getParentIndex(childIndex) {
    /* 0-based index */
    return Math.floor((childIndex - 1) / 2);
  }

  getChildrenIndex(parentIndex) {
    /* 0-based index */
    return [parentIndex * 2 + 1, parentIndex * 2 + 2];
  }

  push(item) {
    console.log(`* push(${item})`);
    this.heap.push(item);

    let childIndex = this.size() - 1;
    let parentIndex = this.getParentIndex(childIndex);

    while (childIndex > parentIndex && parentIndex >= 0) {
      if (this.heap[childIndex] < this.heap[parentIndex]) {
        this.swap(childIndex, parentIndex);
        childIndex = parentIndex;
        parentIndex = this.getParentIndex(childIndex);
      } else {
        break;
      }
    }
  }

  pop() {
    this.swap(0, this.size() - 1);
    const item = this.heap.pop();
    console.log(`* pop() -> ${item}`);

    let parentIndex = 0;
    let [leftChildIndex, rightChildIndex] = this.getChildrenIndex(parentIndex);
    const size = this.size();

    while (parentIndex < size) {
      if (
        leftChildIndex < size &&
        rightChildIndex < size &&
        this.heap[leftChildIndex] < this.heap[parentIndex] &&
        this.heap[rightChildIndex] < this.heap[parentIndex]
      ) {
        if (this.heap[leftChildIndex] < this.heap[rightChildIndex]) {
          this.swap(leftChildIndex, parentIndex);
          parentIndex = leftChildIndex;
        } else {
          this.swap(rightChildIndex, parentIndex);
          parentIndex = rightChildIndex;
        }
      } else if (
        leftChildIndex < size &&
        this.heap[leftChildIndex] < this.heap[parentIndex]
      ) {
        this.swap(leftChildIndex, parentIndex);
        parentIndex = leftChildIndex;
      } else if (
        rightChildIndex < size &&
        this.heap[rightChildIndex] < this.heap[parentIndex]
      ) {
        this.swap(rightChildIndex, parentIndex);
        parentIndex = rightChildIndex;
      } else {
        break;
      }

      [leftChildIndex, rightChildIndex] = this.getChildrenIndex(parentIndex);
    }

    return item;
  }
}
