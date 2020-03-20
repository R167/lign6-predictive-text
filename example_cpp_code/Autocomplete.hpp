/**
 *  CSE 100 PA2 C++ Autocomplete
*/

#ifndef AUTOCOMPLETE_HPP
#define AUTOCOMPLETE_HPP

#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <stack>
#include <tuple>

using namespace std;

/**
 *  You may implement this class as either a mulit-way trie
 *  or a ternary search trie.
 *
 *  You may not use std::map in this implementation
 */
class Autocomplete {
  private:
    class Node {
      public:
        unordered_map<char, Node *> map;
        int count;

        Node() {
          map = unordered_map<char, Node *>();
          count = 0;
        }

        ~Node() {
          for (auto vals : map) {
            delete vals.second;
          }
        }
    };

    Node * root;

  public:

    /*
    Create an Autocomplete object.
    This object should be trained on the corpus vector
    That is - the predictCompletions() function below should pull autocomplete
    suggestions from this vector
    This vector will likely contain duplicates.
    This duplication should be your gauge of frequencey.

    Input: corpus - the corpus of words to learn from.
    Assume preprocessing has been done for you on this! E.g.
    if one of the words is "dán't", assume that each of those characters
    should be included in your trie and don't modify that word any further
    */
    Autocomplete(const vector<string> &corpus) {
      root = new Node();

      Node * nxt;
      for (string const &word : corpus) {
        Node * working = root;
        for (char c : word) {
          nxt = working->map[c];
          if (nxt == nullptr) {
            nxt = working->map[c] = new Node();
          }
          working = nxt;
        }
        working->count++;
      }
    };

    /* Return up to 10 of the most frequent completions
     * of the prefix, such that the completions are words in the dictionary.
     * These completions should be listed from most frequent to least.
     * If there are fewer than 10 legal completions, this
     * function returns a vector with as many completions as possible.
     * Otherwise, 10 completions should be returned.
     * If no completions exist, then the function returns a vector of size 0.
     * The prefix itself might be included in the returned words if the prefix
     * is a word (and is among the 10 most frequent completions
     * of the prefix)
     * If you need to choose between two or more completions which have the same frequency,
     * choose the one that comes first in alphabetical order.
     *
     * Inputs: prefix. The prefix to be completed. Must be of length >= 1.
     * Return: the vector of completions
     */
    vector<string> predictCompletions(const string &prefix) const {
      if (prefix == "") {
        return {};
      }

      Node * start = root;
      for (char c : prefix) {
        auto element = start->map.find(c);
        if (element == start->map.end()) {
          return {};
        }
        start = element->second;
      }

      vector<pair<int, string>> words;
      stack<pair<Node *, string>> stk;
      stk.push(make_pair(start, prefix));

      Node * latest;
      string starter;

      while (!stk.empty()) {
        tie(latest, starter) = stk.top();
        stk.pop();

        if (latest->count > 0) {
          // Multiply by -1 to get proper sorting
          words.push_back(make_pair(latest->count * -1, starter));
        }
        for (auto elm : latest->map) {
          stk.push(make_pair(elm.second, starter + elm.first));
        }
      }

      sort(words.begin(), words.end());

      vector<string> ret(10);

      for (unsigned int i = 0; i < 10 && i < words.size(); i++) {
        ret.push_back(words[i].second);
      }

      return ret;
    };

    /* Destructor */
    ~Autocomplete() {
      delete root;
    };
};

#endif // AUTOCOMPLETE_HPP
