from django.db import models

class Search(models.Model):
    name = models.CharField('お名前', max_length=50)
    content = models.TextField('内容', max_length=140)

    def __str__(self):
        return self.name

class Card( models.Model ):
    cardID = models.IntegerField( 'カードID' )
    image = models.ImageField( '画像', upload_to = '' )
    name = models.CharField( 'カード名' , max_length = 255 )
    rare = models.CharField( 'レア度' )
    cardType = models.CharField( 'カードタイプ' , max_length = 255 )
    element = models.CharField( '属性', max_length = 255 )
    kronos = models.IntegerField( 'クロノス' )
    powerCost = models.IntegerField( 'コスト' )
    sendToPower = models.IntegerField( 'SToP', default = 0  )
    nightPower = models.IntegerField( 'NIGHT', blank = True, null = True )
    dayPower = models.IntegerField( 'DAY', blank = True, null = True )
    skillType = models.CharField( '能力タイプ', max_length = 255, blank = True, null = True )
    skillText = models.TextField( '能力', max_length = 255, blank = True, null = True )

    def __str__(self):
        return '< id : ' + str( self.id ) + ', cardID : ' + str( self.cardID ) + ', name : ' + self.name + ' >'