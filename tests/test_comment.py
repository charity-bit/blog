import unittest

from app.models import Post,User,Comment


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_nyanchera = User(username='_nyanchera', password='aaaaaaaa', email='charitynyanchera@gmail.com')
        self.user = User(username='Lila', password='aaaaaaaa', email='lila@gmail.com')
        
        self.new_post= Post(id=1, title='Protoje', text='Oje Ken Ollivierre (born 14 June 1981), popularly known as Protoje, is a contemporary reggae singer and songwriter from Jamaica.', author=self.user_nyanchera.id)
        self.new_comment = Comment(comment = "His music is good", post_id = self.new_post.id)


    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'Protoje')
        self.assertEquals(self.new_post.text, 'Oje Ken Ollivierre (born 14 June 1981), popularly known as Protoje, is a contemporary reggae singer and songwriter from Jamaica.')
        self.assertEquals(self.new_poat.author, self.user_nyanchera)

    def test_save_post(self):
        self.new_blog.save_post()
        self.assertTrue(len(Post.query.all()) > 0)
