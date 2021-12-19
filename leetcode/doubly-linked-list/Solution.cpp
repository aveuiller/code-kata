// See https://leetcode.com/explore/learn/card/linked-list/210/doubly-linked-list/1294/

class MyLinkedListNode {
    MyLinkedListNode *_next;
    MyLinkedListNode *_prev;
    int _val;
    public:

    MyLinkedListNode(int val) {
        _val = val;
        _next = nullptr;
        _prev = nullptr;
    }

    MyLinkedListNode(int val, MyLinkedListNode *next) {
        _val = val;
        _next = next;
        _prev = nullptr;
    }

    MyLinkedListNode(int val, MyLinkedListNode *next,  MyLinkedListNode *prev) {
        _val = val;
        _next = next;
        _prev = prev;
    }

    int getValue() const {
        return _val;
    }

    void setValue(int val) {
        _val = val;
    }

    MyLinkedListNode* getNext() const {
        return _next;
    }

    void setNext(MyLinkedListNode* next) {
        _next = next;
    }

    MyLinkedListNode* getPrev() const {
        return _prev;
    }

    void setPrev(MyLinkedListNode* prev) {
        _prev = prev;
    }
};

class MyLinkedList {
    MyLinkedListNode *_head = nullptr;
    MyLinkedListNode *_tail = nullptr;

    MyLinkedListNode* nodeAtIndex(int index) const {
//        cout << "nodeAtIndex(" << index << ")" << endl;
        MyLinkedListNode *node = _head;
        if (index < 0) {
            return nullptr;
        }

        for (int i = 0; i < index; i++) {
            if (node != nullptr){
                node = node->getNext();
            } else {
                break;
            }
        }

        return node;
    }

    void updateTail(MyLinkedListNode *node) {
//        cout << "updateTail(" << node << ")" << endl;
        if (node != nullptr && node->getNext() == nullptr) {
            _tail = node;
        }
    }

    MyLinkedListNode* findTail(MyLinkedListNode *node) const {
//        cout << "findTail(" << node << ")" << endl;
        if (node == nullptr) {
            return node;
        }

        while (node->getNext() != nullptr) {
            node = node->getNext();
        }
        return node;
    }

    public:
    MyLinkedList() {

    }

    void print() {
//        MyLinkedListNode *node = _head;
//        while(node != nullptr) {
//            int prevVal = node->getPrev() == nullptr ? -1 : node->getPrev()->getValue();
//            int nextVal = node->getNext() == nullptr ? -1 : node->getNext()->getValue();
//
//            cout << node->getValue() << "(prev:" << prevVal << ", next: " << nextVal << ") ";
//            node = node->getNext();
//        }
//        cout << endl;
    }

    int get(int index) {
//        cout << "get(" << index << ")" << endl;
        MyLinkedListNode *node = nodeAtIndex(index);
        if (node == nullptr) {
            return -1;
        }
        return node->getValue();
    }

    MyLinkedListNode* getTail() {
//        cout << "getTail()" << endl;
        if (_tail == nullptr) {
            updateTail(findTail(_head));
        }
        return _tail;
    }

    void addAtHead(int val) {
//        cout << "addAtHead(" << val << ")" << endl;
        MyLinkedListNode *newHead = new MyLinkedListNode(val, _head);
        if (_head != nullptr) {
            _head->setPrev(newHead);
        }
        _head = newHead;
        if (newHead->getNext() == nullptr) {
            _tail = newHead;
        }
        print();
    }

    void addAtTail(int val) {
//        cout << "addAtTail(" << val << ")" << endl;
        if (getTail() == nullptr) {
            addAtHead(val);
        } else {
            MyLinkedListNode *newTail = new MyLinkedListNode(val);
            _tail->setNext(newTail);
            newTail->setPrev(_tail);
            _tail = newTail;
        }
        print();
    }

    void addAtIndex(int index, int val) {
//        cout << "addAtIndex(" << index << "," << val << ")" << endl;
        MyLinkedListNode *previous = nodeAtIndex(index - 1);
        MyLinkedListNode *replaced = nodeAtIndex(index);
        MyLinkedListNode *newNode = new MyLinkedListNode(val);

        // No node found, only valid if first element.
        if (previous == nullptr && replaced == nullptr) {
            // Special case: first element & first index
            if (_head == nullptr && index == 0) {
                _head = newNode;
                _tail = newNode;
            }
            return;
        }

        // Previous node exists: appending
        if (previous != nullptr) {
             previous->setNext(newNode);
             newNode->setPrev(previous);
             if (replaced == nullptr) {
                _tail = newNode;
             }
        }

        // Replaced node existing: prepending
        if (replaced != nullptr){
            replaced->setPrev(newNode);
            newNode->setNext(replaced);
            if (previous == nullptr) {
                _head = newNode;
            }
        }
        print();
    }

    void deleteAtIndex(int index) {
//        cout << "deleteAtIndex(" << index << ")" << endl;
        MyLinkedListNode *deletedNode = nodeAtIndex(index);
        if (deletedNode == nullptr) {
            return;
        }

        MyLinkedListNode *prevNode = deletedNode->getPrev();
        MyLinkedListNode *nextNode = deletedNode->getNext();

        if (prevNode == nullptr) {
            _head = nextNode;
        } else {
            prevNode->setNext(nextNode);
        }

        if (nextNode == nullptr) {
            _tail = prevNode;
        } else {
            nextNode->setPrev(prevNode);
        }
        delete(deletedNode);
        print();
    }
};

/**
 * Test cases:
 *
 * ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
   [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
 *
 * ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
   [[],[1],[3],[1,2],[1],[1],[1]]
 *
 * ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
   [[],[0,10],[0,20],[1,30],[0]]
 *
 * ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
   [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
 *
 * ["MyLinkedList","addAtIndex","get"]
   [[],[1,0],[0]]
 */

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */