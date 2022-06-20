class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL)
        {
            return list2;
        }
        if(list2 == NULL)
        {
            return list1;
        }
        else
        {
           ListNode *ptr = list1;
            if(list1->val <= list2->val)
            {
                list1 = list1->next;
            }
            else
            {
                ptr = list2;
                list2 = list2->next;
            }
            ListNode *curr = ptr;
            while(list1 && list2)
            {
                if(list1->val <= list2->val)
                {
                    curr->next = list1;
                    list1 = list1->next;
                }
                else
                {
                    curr->next = list2;
                    list2 = list2->next;
                }
                curr = curr->next;
            }
            if(list1)
            {
                curr->next = list1;
            }
            if(list2)
            {
                curr->next = list2;
            }
            return ptr;
        }
    }
};
