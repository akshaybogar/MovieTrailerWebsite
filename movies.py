'''
This file creates 9 instances of movie class
'''
import fresh_tomatoes
import movie_class


# Movie name: vikramvedha
vikramvedha = movie_class.Movie('VikramVedha',
                                'A badass cop Vikram leads a special task'
                                ' force formed to eliminate a kickass Vedha\'s'
                                'gang running amok on the streets of Chennai,'
                                ' making mockery of Law and Order. An'
                                ' encounter planned by a Vikram\'s…',
                                'https://www.bing.com/th?id=OIP.ns8C96g2qctV45'
                                'kpEAYyWwHaHn&w=163&h=168&c=7&o=5&pid=1.7',
                                'https://www.youtube.com/watch?v=1sVr-uWZPjE',
                                '8.8/10',
                                'Suspense-Thriller')

# Movie name:andhadhun
andhadhun = movie_class.Movie('Andhadhun',
                              'A series of mysterious events take place in the'
                              'life of a blind pianist (Ayushmann Khurrana).'
                              'Now, he must report a crime that he never'
                              'actually witnessed.',
                              'https://in.bmscdn.com/iedb/movies/images'
                              '/website/poster/large/andhadhun-et00077959'
                              '-19-06-2018-12-49-25.jpg',
                              'https://www.youtube.com/watch?v=2iVYI99VGaw',
                              '9.1/10',
                              'Thriller-Crime')

# Movie name:badhaai ho
badhaaiho = movie_class.Movie('Badhaai ho',
                              'A 25-year-old man tries to suppress his '
                              'embarrassment when his mother announces'
                              'that she is pregnant.',
                              'https://encrypted-tbn0.gstatic.com/images'
                              '?q=tbn:ANd9GcSoDxlTGYK5ULTsIvhTXJrMBz1nm'
                              'jUIb4Vcn_uEkWjpIzzomVLHog',
                              'https://www.youtube.com/watch?v=unAljCZMQYw',
                              '8.3/10',
                              'Comedy-Drama')

# Movie name:zero
zero = movie_class.Movie('Zero',
                         'Raj, a man of short stature dreams of dating'
                         'a specific superstar. He doesn\'t know what to'
                         'expect in return, but what he does know is that true'
                         'love comes in various forms.',
                         'https://static.toiimg.com/photo/62333886.cms',
                         'https://www.youtube.com/watch?v=Ru4lEmhHTF4',
                         'No ratings yet',
                         'Romance')

# Movie name:thugs of hindustan
toh = movie_class.Movie('Thugs of Hindustan',
                        'Based on Philip Meadows Taylor\'s 1839 novel'
                        'Confessions of a Thug, the movie tells us about a'
                        'thug named Ameer Ali and his gang, whose nefarious'
                        'ways posed a serious challenge to the British Empire'
                        'in India between 1790 and 1805.',
                        'https://www.hindustantimes.com/rf/image_size_960x540'
                        '/HT/p2/2018/09/26/Pictures/_4a1e3da4-c164-11e8-9e8c'
                        '-b17643e39fb5.jpg',
                        'https://www.youtube.com/watch?v=zI-Pux4uaqM',
                        'No ratings yet',
                        'Period Movie')

# Movie name:stree
stree = movie_class.Movie('Stree',
                          'In the small town of Chanderi, the menfolk live in'
                          'fear of an evil spirit named "Stree" who abducts'
                          'men in the night. Based on the urban legend of'
                          '"Nale Ba" that went viral in Karnataka in the'
                          '1990s.',
                          'https://www.bing.com/th?id=OIP.d2Hdg0_BpR3SG9EKid'
                          'NJyAHaEH&w=256&h=160&c=7&o=5&pid=1.7',
                          'https://www.youtube.com/watch?v=gzeaGcLLl_A',
                          '8.3/10',
                          'Horror-Comedy')

# Movie name:karwaan
karwaan = movie_class.Movie('Karwaan',
                            'The movie depicts a journey carried out from'
                            'Bangalore to Kochi by two friends, the reserved'
                            'Avinash played by Dulquer Salmaan, and his friend'
                            'Shaukat played by Irrfan Khan with a lighter'
                            'take on life…',
                            'https://tse4.mm.bing.net/th?id=OIP.'
                            '2VaKv9Fhmngtm5nz-nItHgHaFF&pid=Api',
                            'https://www.youtube.com/watch?v=IUCeN7kelXs',
                            '7.7/10',
                            'Adventure-Drama')

# Movie name:manmarziyaan
manmarziyan = movie_class.Movie('Manmarziyaan',
                                'Rumi and Vicky are love birds where Rumi'
                                'convinces her parents to let her marry her'
                                'love, while Vicky is commitment phobic. In'
                                'comes Robbie, a much well-settled NRI who'
                                'falls for Rumi. Whom will she… ',
                                'https://www.bing.com/th?id=OIP.1TlksE7uw'
                                'Y9vROyUNZQFygHaLH&w=117&h=177&c=7&o='
                                '5&pid=1.7',
                                'https://www.youtube.com/watch?v=ToxnuakJrqE',
                                '7.1/10',
                                'Romance')

# Movie name:baazaar
baazaar = movie_class.Movie('Baazaar',
                            'Baazaar is a 2018 film starring Saif Ali Khan,'
                            'Chitrangada Singh and Radhika Apte. With a plot'
                            'revolving around stock-trading, the film,'
                            'according to director Gauravv K. Chawla\'s is'
                            'about making it in… ',
                            'https://www.bing.com/th?id=OIP.uOZ6BG-'
                            '13hZy8mS5tFb_fAHaJ4&w=181&h=241&c=7&o=5&pid=1.7',
                            'https://www.youtube.com/watch?v=Pb7iJnIWzNk',
                            '7.2/10',
                            'Thriller')

# Creating a list consisting of all movies
movies = [vikramvedha, andhadhun, badhaaiho, zero, toh, stree, karwaan,
          manmarziyan, baazaar]
# Passing the list moviess to generate HTML page
fresh_tomatoes.open_movies_page(movies)
