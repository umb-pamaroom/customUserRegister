from django.forms import ModelForm
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['dateData', 'discovery', 'tired', 'happy', 'best', 'tomorrow', 'dislike','other', 'summarize', 'breakfast', 'breakfastName', 'breakfastEvaluation', 'lunch','lunchName', 'lunchEvaluation', 'dinner', 'dinnerName' , 'dinnerEvaluation' , 'snack', 'snackName', 'snackEvaluation', 'mealComment']
        labels = {
            'dateData': '日付',
            'discovery': '新しい発見',
            'tired': '一番印象に残ったこと',
            'dislike': '改善点',
            'happy': '嬉しかったこと',
            'best': '頑張ったこと',
            'tomorrow': '明日したいこと',
            'other': 'その他',
            'summarize': '1日のまとめ',
            'breakfast': '朝食',
            'breakfastName': '朝食名',
            'breakfastEvaluation': '朝食評価',
            'lunch': '昼食',
            'lunchName': '昼食名',
            'lunchEvaluation': '昼食評価',
            'dinner': '夕食',
            'dinnerName': '夕食名',
            'dinnerEvaluation': '夕食評価',
            'snack': '間食',
            'snackName': '間食名',
            'snackEvaluation': '間食評価',
            'mealComment': '食事へのコメント',
        }
        
