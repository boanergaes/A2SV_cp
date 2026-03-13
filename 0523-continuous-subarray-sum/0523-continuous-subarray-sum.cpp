class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> ref;
        ref[0] = -1;
        int running = 0;

        for (int i = 0; i < nums.size(); i++) {
            running += nums[i];
            if (ref.contains(running % k)) {
                if (i - ref[running % k] > 1) return true;
            } else ref[running % k] = i;
        }

        return false;
    }
};