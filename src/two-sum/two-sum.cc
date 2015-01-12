class Solution {

public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    map<int, int> hashmap;
    vector<int> result;
    for (int i = 0; i < numbers.size(); i++) {
      if (hashmap.find(numbers[i]) == hashmap.end()) {
        hashmap[target - numbers[i]] = i;
      } else {
        result.push_back(hashmap[numbers[i]] + 1);
        result.push_back(i + 1);
        break;
      }
    }
    return result;
  }
};
