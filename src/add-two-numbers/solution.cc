/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carryOver = 0;
        int l1Val = 0;
        int l2Val = 0;
        int sum = 0;
        ListNode *head = NULL;
        ListNode **tail = &head;
        while (l1 != NULL or l2 != NULL) {
            l1Val = getValueAndMove(&l1);
            l2Val = getValueAndMove(&l2);
            sum = l1Val + l2Val + carryOver;
            carryOver = sum / 10;
            ListNode *tNode = new ListNode(sum % 10);
            *tail = tNode;
            tail = &tNode->next;
        }
        if (carryOver >0) {
            ListNode *tNode = new ListNode(carryOver);
            *tail = tNode;
        }
        return head;
    } 
private:
    int getValueAndMove(ListNode **l) {
        int r = 0;
        if (*l != NULL) {
            r = (*l)->val;
            *l = (*l)->next;
        }
        return r;
    }
};
