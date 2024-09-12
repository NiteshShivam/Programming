/*
https://leetcode.com/problems/spiral-matrix-iv/description/

mik-video:
https://youtu.be/h-3aM0bEUZ8
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> result(m,vector<int>(n,-1));
        int left=0;
        int right =n-1;
        int top=0;
        int down=m-1;
        int direction =0;
        while(left<=right && top<=down && head!=NULL){
            if(direction==0){
                int j=left;
                while(j<=right && head){
                    result[top][j]=head->val;
                    head=head->next;
                    j+=1;
                }
                top++;
            }
            else if(direction==1){
                int j=top;
                while(j<=down && head){
                    result[j][right] = head->val;
                    head=head->next;
                    j++;
                }
                right--;
            }
            else if(direction==2){
                int j=right;
                while(j>=left && head){
                    result[down][j] = head->val;
                    head=head->next;
                    j--;
                }
                down--;
            }
            else if(direction==3){
                int j=down;
                while(j>=top && head){
                    result[j][left] = head->val;
                    head=head->next;
                    j--;
                  

                }
                left++;
            }
            direction = (direction+1)%4;
        }
        return result;
    }
};
