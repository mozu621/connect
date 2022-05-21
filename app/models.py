from django.db import models
from django.conf import settings


# 引数　instance→profileclassからできたインスタンス、filename→フロントエンドから受け取ったファイルネーム
def upload_avatar_path(instance, filename):
    ext = filename.split('.')[-1]  # 拡張子を格納→splitで分離　配列の一番最後の−１で取得している
    return '/'.join(['avatars', str(instance.profileUser.id)+str(instance.nickName)+str(".")+str(ext)])


def upload_portfolio_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['portfolios', str(instance.author.id)+str(instance.title)+str(".")+str(ext)])


class Profile(models.Model):
    nickName = models.CharField(max_length=20)
    #追加
    introduction = models.CharField(max_length=300, blank=True, null=True)
    # ここまで
    profileUser = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profileUser',
        # user削除時、連動削除
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True,
                            upload_to=upload_avatar_path)

    def __str__(self):
        return self.nickName




class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200, unique=True, blank=True, null=True)
    content = models.CharField(max_length=300, blank=True)


    author = models.ForeignKey(
        # author(user_id)に結びつくPortfolio(多),protfolioに結びつくauthor(一)
        settings.AUTH_USER_MODEL, related_name='author',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True,
                            upload_to=upload_portfolio_path)

    def __str__(self):
        return self.title


class Like(models.Model):
    likeUser = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='likeUser',
        on_delete=models.CASCADE
    )
    likePortfolio = models.ForeignKey(
        Portfolio, related_name='likePortfolio', on_delete=models.CASCADE)

    def __int__(self):
        return self.likeUser , self.likePortfolio, self.id


class Comment(models.Model):
    text = models.CharField(max_length=100)
    commentUser = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='commentUser',
        on_delete=models.CASCADE
    )
    commentPortfolio = models.ForeignKey(
        Portfolio, related_name='commentPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# 追加
class Tag(models.Model):
    tagname = models.CharField('タグ', max_length=30)
    tagPortfolio = models.ForeignKey(
        Portfolio, related_name='tagPortfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.tagname        
