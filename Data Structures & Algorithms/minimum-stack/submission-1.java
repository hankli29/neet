class MinStack {
    List<Integer> stack;
    List<Integer> min;
    public MinStack() {
        stack = new ArrayList<>();
        min = new ArrayList<>();
    }
    
    public void push(int val) {
        stack.add(val);
        if (min.size() == 0){
            min.add(val);
        } else {
            if (val <= min.get(min.size()-1)) {
                min.add(val);
            }
        }
    }
    
    public void pop() {
        int temp = stack.get(stack.size()-1);
        stack.remove(stack.size()-1);
        if (min.get(min.size()-1) == temp) {
            min.remove(min.size()-1);
        }

    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return min.get(min.size()-1);
    }
}
