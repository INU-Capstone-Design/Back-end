from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("ko_w2v_model") # 모델 로드

Model = Namespace(
    name="Model",
    description="키워드 예측을 위한 API"
)

jwt_fields = Model.model('JWT', {
    'Authorization': fields.String(description='Authorization which you must inclued in header', required=True, example="eyJ0e~~~~~~~~~")
})

@Model.route('/<string:ko_word>', methods=['GET'])
class WordPredict(Resource):
    @Model.expect(jwt_fields)
    @Model.doc(responses={200: 'Success'})
    @Model.doc(responses={500: 'Out of Vocabulary'})
    @jwt_required()
    def get(self, ko_word:str):
        try: # 모델에 단어 입력
            result = model.most_similar(ko_word)
            words = [word[0] for word in result]
            return {
                'message': words[:5]
            }, 200
            
        except: # OOP 발생
            return {
                'message': 'Out Of Vocabulary'
            }, 500