import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# device = torch.device("cpu")


def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False

classes = ['drink water', 'eat meal/snack',
           'brushing teeth', 'brushing hair',
           'drop', 'pickup',
           'throw', 'sitting down',
           'standing up', 'clapping',
           'reading', 'writing',
           'tear up paper', 'wear jacket',
           'take off jacket', 'wear a shoe',
           'take off a shoe', "wear on glasses",
           'take off glasses', 'put on a hat/cap',
           'take off a hat/cap', 'cheer up',
           'hand waving', 'kicking something',
           'reach into pocket', 'hopping (one foot jumping)',
           'jump up', 'make a phone call/answer phone',
           'playing with phone/tablet', 'typing on keyboard',
           'pointing to something with finger', 'taking a selfie',
           'check time (watch)', 'rub hands together',
           'nod head/bow', 'shake head',
           'wipe face', 'salute',
           'put the palms together', 'cross hands in front',
           'sneeze/couggh', 'staggering',
           'falling', 'touch head',
           'touch chest', 'touch back',
           'touch neck', 'nausea or vomiting',
           'use a fan', 'punching/slapping other person',
           'kicking other person', 'pushing other person',
           'pat on back of other person', 'point finger at other person',
           'hugging other person', 'giving something to other person',
           'touch other person pocket', 'handshaking',
           'walk toward other', 'walk apart from each other']
