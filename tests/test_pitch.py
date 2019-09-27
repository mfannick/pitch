from app.models import Review,User
from app import db

def setUp(self):
        self.user_annick = User(username = 'annick',password = 'escofavi', email = 'mfannick1@gmail.com')
        self.pitch= Review(pitchId=1,pitchWrite='technology',pitchTitle="promotion",category='promotion',user = self.user_annick )

def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
def test_check_instance_variables(self):
        self.assertEquals(self.pitch.id,1)
        self.assertEquals(self.pitch.pitchWrite,'technology')
        self.assertEquals(self.pitch.pitchTitle,'promotion')
        self.assertEquals(self.pitch.category,'promotion')
        self.assertEquals(self.pitch.userId.user,self.user_annick)
def test_savePitch(self):
        self.pitch.savePitch()
        self.assertTrue(len(Pitch.query.all())>0)
def test_getPitch_by_id(self):

        self.pitch.savePitch()
        gotPitch= pitch.getPitch(1)
        self.assertTrue(len(gotPitches) == 1)


    