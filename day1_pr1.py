import string
text = input('input message : ')

#punctuation은 문장부호 의미. maketrans는 문장부호 제거하는 함수, translate 함수는 변환한 것을 characters에 저장
characters = len(text.translate(str.maketrans('', '', string.punctuation)))

words = text.split() # 공백기준으로 잘라서 리스트로 저장
word_count = len(words)

sentences = text.split(",")
sentences = [sentence for sentence in sentences if sentence] # sentences리스트에서 공백등을 제거하여 새 리스트에 저장. if문의 의미는 비어있거나 blank이면 안된다는 뜻
#리스트 컴프리헨션은 기존 리스트의 각 요소에 특정 조건 또는 변환을 적용하여 새 리스트를 만드는 방법임.
