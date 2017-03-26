
# coding: utf-8

# In[1]:

class Autocomplete():
	def __init__(self, word_list = []):
		self.children = {}
		self.word_list = word_list
		self.is_word_end = False

	def findWordWithPrefix(self, pattern):
		findWordWithPrefix_results = []
		if self.is_word_end:
			findWordWithPrefix_results.append(pattern)
		for (char, node) in self.children.items():
			findWordWithPrefix_results.extend(node.findWordWithPrefix(pattern + char))
		return findWordWithPrefix_results

	def findPattern(self, pattern):
		node = self
		findPattern_results = []
		for char in pattern:
			if char not in node.children:
				return None
			node = node.children[char]
		findPattern_results = list(node.findWordWithPrefix(pattern))
		return findPattern_results
		
	def insertWord(self, word):
		for char in word:
			if char not in self.children:
				self.children[char]= Autocomplete()
			self = self.children[char]
		self.is_word_end = True	
		
	def find(self, pattern):
		find_results = []
		for word in word_list:
			self.insertWord(word)
		find_results = self.findPattern(pattern)
		if not find_results:
			print("None")
		return find_results


# In[2]:

if __name__=="__main__":
	word_list = ['aardvark', 'altimeter', 'apotactic', 'bagonet', 'boatlip', 'carburant', 'chyliferous', 'consonance', 'cyclospondylic', 'dictyostele', 'echelon', 'estadal', 'flaunty', 'gesneriaceous', 
'hygienic', 'infracentral', 'jipijapa', 'lipoceratous', 'melanthaceae']
	newAutoC = Autocomplete(word_list)
	ResNewAutoC = newAutoC.find('a')


# In[3]:

ResNewAutoC


# In[4]:

if __name__=="__main__":
	word_list = ['angiohydrotomy', 'angiospermal', 'anglist', 'angularization', 'anhungry', 'animalcule', 'anisaldehyde', 'anisometric', 'ankylenteron', 'annette']
	newAutoC = Autocomplete(word_list)
	ResNewAutoC = newAutoC.find('ani')


# In[5]:

ResNewAutoC


# In[6]:

if __name__=="__main__":
	word_list = ['bagonet', 'consonance', 'estadal', 'hygienic', 'melanthaceae', 'overwander', 'prototypographer', 'siphonocladales', 'transferography', 'venturesomeness']
	newAutoC = Autocomplete(word_list)
	ResNewAutoC = newAutoC.find('venture')


# In[7]:

ResNewAutoC


# In[8]:

if __name__=="__main__":
	word_list = ['anisaldehyde', 'anisometric', 'ankylenteron']
	newAutoC = Autocomplete(word_list)
	ResNewAutoC = newAutoC.find('foobar')


# In[ ]:



