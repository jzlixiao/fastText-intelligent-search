from app_rank.model.seasion_type_rank_model import fit_season_rank
from app_rank.model.city_type_rank_model import fit_city_rank
from app_rank.model.colothing_rank_model import clothing_rank


# 训练model
def fit_rank():
    clothing_result = clothing_rank()
    season_fit_result = fit_season_rank()
    city_fit_result = fit_city_rank()
    if season_fit_result == '1' and city_fit_result == '1' and clothing_result == '1':
        return '1'
    else:
        return '0'
