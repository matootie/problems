class RandomizedSet {
    data: { [key: number]: number }
    dataset: number[]

    constructor() {
        this.data = {}
        this.dataset = []
    }

    insert(val: number): boolean {
        if (typeof (this.data[val]) === "number") {
            return false
        }
        const index = this.dataset.push(val) - 1
        this.data[val] = index
        return true
    }

    remove(val: number): boolean {
        if (typeof (this.data[val]) === "number") {
            // Get the last value added.
            const lastVal = this.dataset[this.dataset.length - 1]
            // Get the index of the value we want to remove.
            const currIndex = this.data[val]
            // Place the last value in the index of the value to remove.
            this.dataset[currIndex] = lastVal
            // Update the index in the map.
            this.data[lastVal] = currIndex
            // Remove the old entry in the map.
            delete this.data[val]
            // Remove the last element in the array.
            this.dataset.pop()

            return true
        }
        return false
    }

    getRandom(): number {
        const randomIndex = Math.floor(Math.random() * this.dataset.length)
        return this.dataset[randomIndex]
    }
}
