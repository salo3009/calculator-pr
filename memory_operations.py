class Memory:
    def __init__(self):
        self._memory = 0
        self._memory_slots = {} 
    
    def memory_add(self, value):
        self._memory += float(value)
    
    def memory_subtract(self, value):
        self._memory -= float(value)
    
    def memory_recall(self):
        return self._memory
    
    def memory_clear(self):

        self._memory = 0
    
    def memory_store(self, value):
        self._memory = float(value)

    def memory_slot_store(self, slot, value):
        self._memory_slots[slot] = float(value)
    
    def memory_slot_recall(self, slot):
        return self._memory_slots.get(slot, 0)
    
    def memory_slot_clear(self, slot):
        if slot in self._memory_slots:
            del self._memory_slots[slot]
    
    def memory_slot_add(self, slot, value):
        if slot not in self._memory_slots:
            self._memory_slots[slot] = 0
        self._memory_slots[slot] += float(value)
    
    def get_memory_status(self):
        status = f"M: {self._memory}"
        for slot, value in self._memory_slots.items():
            status += f", {slot}: {value}"
        return status
    
    def clear_all_memory(self):
        self._memory = 0
        self._memory_slots.clear()
