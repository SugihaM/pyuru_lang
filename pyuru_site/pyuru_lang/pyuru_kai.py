from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

class Pyuru_Lang_Translation:
    def pyuru_lang_translation(self, val):
        return_string = ''
        #一番最初の単語をみるためのフラグ
        flag = True
        #前の文章に伸ばし棒がついてないか確認するためのフラグ
        before = True
        #形態素解析で分けた分だけ回す
        for token in tokenizer.tokenize(val):
            #変数ども
            string = token.part_of_speech.split(',')[0]
            string2 = token.part_of_speech.split(',')[1]
            string3 = token.part_of_speech.split(',')[2]
            type = token.infl_type
            form = token.infl_form
            #一番最初の単語に対しての変換
            if flag:
                if string.startswith('感動'):
                    return_string += 'ぴゅる〜'
                    print('ぴゅる〜', end='')

                #記号の時の場合分け忘れてまちた
                elif string.startswith('記号'):
                    return_string += token.surface
                    print(token.surface, end ='')

                elif form.startswith('連用タ接続') :
                    return_string += 'ぴゅ〜る'
                    print('ぴゅ〜る', end='')

                else:
                    return_string += 'ぴゅる'
                    print('ぴゅる', end ='')

                flag = False
            #二番目以降の変換
            else:
                if string2.startswith('連体化') or string2.startswith('接続助詞') or type.startswith('特殊・タ'):
                    return_string += ''
                    print('', end ='')
                    before = True

                elif string.startswith('記号') or token.surface in 'ぴゅる' or token.surface in 'ぴゅ〜る':
                    return_string += token.surface
                    print(token.surface, end='')
                    before = True

                elif string.startswith('名詞') and string2.startswith('副詞可能'):
                    return_string += 'ーるる'
                    print('ーるる',end ='')
                    before = True

                elif string2.startswith('格助詞') and before or string.startswith('助動詞') and form.startswith('基本形') and before:
                    return_string += 'ー'
                    print('ー',end ='')
                    before = False

                elif string.startswith('名詞') and not string2.startswith('一般') and not string2.startswith('非自立') and not string2.startswith('サ変接続') and before:
                    return_string += 'るー'
                    print('るー', end='')
                    before = False

                elif string2.startswith('終助詞') and before:
                    return_string += 'っる〜'
                    print('っる〜', end='')
                    before = False

                elif form.startswith('連用形') or string.startswith('動詞') and string2.startswith('非自立'):
                    return_string += 'るる'
                    print('るる', end ='')
                    before = True

                elif string.startswith('動詞') and not form.startswith('未然形') or form.startswith('連用タ接続'):
                    return_string += 'ぴゅる'
                    print('ぴゅる', end='')
                    before = True

                elif string.startswith('名詞') and string2.startswith('非自立') and string3.startswith('一般'):
                    return_string += 'ぴゅ〜る'
                    print('ぴゅ〜る', end='')
                    before = True

                elif string.startswith('助詞') and string2.startswith('副助詞'):
                    return_string += 'っる'
                    print('っる', end ='')
                    before = True

                else:
                    return_string += 'る'
                    print('る', end='')
                    before = True

        return return_string
