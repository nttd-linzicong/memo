// Last modified at 2018/09/30 9:42

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iomanip>	// for std::setw
#include <utility>	// for std::pair
#include <cstring>
#include <vector>	// You shall not use this lib in your code part

#define RAND_HALF (RAND_MAX)/2



// The frame of class has been provided for you, you may only need to implemnet member functions.
template<class Key, class Val>
class skiplist {
private:
	class _node {
	private:
		// key and val are encapsulated in _data with std::pair
		std::pair<const Key, Val> _data;
		_node **_forward;

		// friend class enables skiplist to access private members of _node
		friend class skiplist;
	public:
		// Constructor of _node, by default key and val are set as NULL (it's for dummy node)
		_node(int height, const Key &key = Key(), const Val &val = Val());
		// Destructor, free the memory allocated by _node
		~_node();
	};

private:
	// Current _level, at least 1, at most _height_limit
	int _level;

	int _height_limit;

	// _head is a dummy node for skiplist
	_node *_head;

public:
	// Constructor, set _height_limit and initialize the skiplist
	skiplist(int height_limit);

	// Destructor, free all the memory allocated by skiplist
	~skiplist();

	// Insert a new node
	int insert(const Key &key, const Val &val);


	// Search a key in skiplist
	bool search(const Key &key);


	// Remove a node with given key. Free all the memory allocated to this node, including its _forward
	bool remove(const Key &key);


	
private:
	// This function has been implemented for you
	// Generate a random level for the node
	// You will need this in insertion
	int randomLevel();

public:
	// This function has been implemented for you
	// This function is for testing and your debugging
	// Display the skiplist list
	// You will need this in debugging. To show the whole picture, output the answer with IO redirection and use a wide screen
	void display();
};
//======================= DO NOT MODIFY CODE ABOVE===========================

//============================ Begin Your Code ==============================

// Assign (key, val) to _data, allocate memory for _forward
template<class Key, class Val>
skiplist<Key, Val>::_node::_node(int height, const Key &key, const Val &val){};


template<class Key, class Val>
skiplist<Key, Val>::_node::~_node(){};


// The initial level is 1
template<class Key, class Val>
skiplist<Key, Val>::skiplist(int height_limit) {};


// Free the whole skiplist
template<class Key, class Val>
skiplist<Key, Val>::~skiplist() {};


// Insert a new node with key & val. Insert by key with increasing order, i.e. from head to tail, the keys of nodes are increasing. For convenience, you can simply use use <, > and == to compare as we will only use int and float for Key type
//		1) If the key does not exist before insertion, insert the new node with key & val in the proper place. Return 0
//		2) If the key exists before insertion, replace the old val with the new val. Return 1
// You will need function randomLevel() when generating a new node
template<class Key, class Val>
int skiplist<Key, Val>::insert(const Key &key, const Val &val) {};


// Search a key in skiplist. Return true if found, else return false
template<class Key, class Val>
bool skiplist<Key, Val>::search(const Key &key) {};


// Remove a node with given key. Free all the memory allocated to this node, including its _forward
// Return true if success, else return false.
template<class Key, class Val>
bool skiplist<Key, Val>::remove(const Key &key) {};



//=========================== End Your Code =================================



//=========================== DO NOT MODIFY CODE BELOW=======================

// Return a new level for your new node
template<class Key, class Val>
int skiplist<Key, Val>::randomLevel() {
	int new_level = 1;
	while (new_level < _height_limit && rand() < RAND_HALF) ++new_level;
	return new_level;
};




template<class Key, class Val>
void skiplist<Key, Val>::display() {
	std::cout << "********* Skiplist ********\n";


	for (int i = _level-1; i >= 0; --i) {
		_node *base = _head->_forward[0];
		_node *curr = _head->_forward[i];

		std::cout << "Level " << i+1 << ": ";
		while (curr != NULL) {
			while (curr != base && base != NULL) {
				std::cout << std::setw(3) << " " << std::setw(1) << " " << std::setw(2) << " " << std::setw(1) << " ";
				base = base->_forward[0];
			}

			if (curr == base) {
				std::cout << std::setw(3) << curr->_data.first << std::setw(1) << ":" << std::setw(2) << curr->_data.second << std::setw(1) << " ";
				base = base->_forward[0];
			}

			
			curr = curr->_forward[i];
		}
		std::cout << "\n" << '\n';
	}
};

void get_input(std::vector<std::string> *tokens, char *inputs) {
	std::string str = inputs;
	std::string token;
	size_t pos;

	while (str.size() != 0) {
		pos = str.find(" ");
		if (pos != std::string::npos) {
			token = str.substr(0, pos);
			str = str.substr(pos + 1);
		}
		else {
			token = str;
			str = "";
		}
		(*tokens).push_back(token);
	}
}

// IO has been provided for you
int main(void)
{
	srand(2);

	char c[20];

	std::cin.getline(c, 20, '\n');
	if (c[0] == '0') {
		skiplist<int, std::string> sl(10);

		while(std::cin.getline(c, 20, '\n')) {
			std::vector<std::string> tokens;
			get_input(&tokens, c);
			if (tokens[0] == "+") {
				sl.insert(atoi(tokens[1].c_str()), tokens[2]);
				std::cout << "insert: " << tokens[1] << ": " << tokens[2] << '\n';
			}
			else if (tokens[0] == "-") {
				sl.remove(atoi(tokens[1].c_str()));
				std::cout << "remove: " << tokens[1] << '\n';
			}
			else if (tokens[0] == "@") {
				std::cout << "search: " << tokens[1] << " " << std::boolalpha << sl.search(atoi(tokens[1].c_str())) << '\n';
			}
			else {
				std::cout << "display:" << '\n';
				sl.display();
			}
		}
	}
	else if (c[0] == '1') {
		skiplist<float, int> sl(10);

		while(std::cin.getline(c, 20, '\n')) {
			std::vector<std::string> tokens;
			get_input(&tokens, c);
			if (tokens[0] == "+") {
				sl.insert(atof(tokens[1].c_str()), atoi(tokens[2].c_str()));
				std::cout << "insert: " << tokens[1] << ": " << tokens[2] << '\n';
			}
			else if (tokens[0] == "-") {
				sl.remove(atof(tokens[1].c_str()));
				std::cout << "remove: " << tokens[1] << '\n';
			}
			else if (tokens[0] == "@") {
				std::cout << "search: " << tokens[1] << " " << std::boolalpha << sl.search(atof(tokens[1].c_str())) << '\n';
			}
			else {
				std::cout << "display:" << '\n';
				sl.display();
			}
		}
	}

	return 0;
}
