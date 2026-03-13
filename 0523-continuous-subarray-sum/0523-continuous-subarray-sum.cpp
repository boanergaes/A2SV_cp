class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> ref;
        ref[0] = -1;
        int running = 0;

        for (int i = 0; i < nums.size(); i++) {
            running += nums[i];
            int r = running % k;
            if (ref.contains(r)) {
                if (i - ref[r] > 1) return true;
            } else ref[r] = i;
        }

        return false;
    }
};