from typing import Dict, List
from json_loader import json_loader

def metadata_func(record: dict) -> dict:
    return {
            # 'id': record.get('id'),
            'oracle_id': record.get('oracle_id'),
            # 'multiverse_ids': record.get('multiverse_ids'),
            # 'mtgo_id': record.get('mtgo_id'),
            # 'mtgo_foil_id': record.get('mtgo_foil_id'),
            # 'tcgplayer_id': record.get('tcgplayer_id'),
            # 'recordmarket_id': record.get('recordmarket_id'),
            'name': record.get('name'),
            # 'lang': record.get('lang'),
            'released_at': record.get('released_at'),
            # 'uri': record.get('uri'),
            # 'scryfall_uri': record.get('scryfall_uri'),
            # 'layout': record.get('layout'),
            # 'highres_image': record.get('highres_image'),
            # 'image_status': record.get('image_status'),
            # 'image_uris': record.get('image_uris'),
            'mana_cost': record.get('mana_cost'),
            'cmc': record.get('cmc'),
            'type_line': record.get('type_line'),
            'oracle_text': record.get('oracle_text'),
            'power': record.get('power'),
            'toughness': record.get('toughness'),
            'colors': record.get('colors'),
            'color_identity': record.get('color_identity'),
            'keywords': record.get('keywords'),
            'legalities': record.get('legalities'),
            'games': record.get('games'),
            # 'reserved': record.get('reserved'),
            # 'foil': record.get('foil'),
            # 'nonfoil': record.get('nonfoil'),
            # 'finishes': record.get('finishes'),
            # 'oversized': record.get('oversized'),
            # 'promo': record.get('promo'),
            # 'reprint': record.get('reprint'),
            # 'variation': record.get('variation'),
            # 'set_id': record.get('set_id'),
            # 'set': record.get('set'),
            'set_name': record.get('set_name'),
            # 'set_type': record.get('set_type'),
            # 'set_uri': record.get('set_uri'),
            # 'set_search_uri': record.get('set_search_uri'),
            # 'scryfall_set_uri': record.get('scryfall_set_uri'),
            # 'rulings_uri': record.get('rulings_uri'),
            # 'prints_search_uri': record.get('prints_search_uri'),
            # 'collector_number': record.get('collector_number'),
            # 'digital': record.get('digital'),
            # 'rarity': record.get('rarity'),
            # 'flavor_text': record.get('flavor_text'),
            # 'record_back_id': record.get('record_back_id'),
            # 'artist': record.get('artist'),
            # 'artist_ids': record.get('artist_ids'),
            # 'illustration_id': record.get('illustration_id'),
            # 'border_color': record.get('border_color'),
            # 'frame': record.get('frame'),
            # 'full_art': record.get('full_art'),
            # 'textless': record.get('textless'),
            # 'booster': record.get('booster'),
            # 'story_spotlight': record.get('story_spotlight'),
            # 'edhrec_rank': record.get('edhrec_rank'),
            # 'prices': record.get('prices'),
            # 'related_uris': record.get('related_uris'),
            # 'purchase_uris': record.get('purchase_uris'),
    }

def process_oracle_text(file_path: str) -> List[Dict]:
    return json_loader(
        file_path=file_path,
        content_key='oracle_id',
        metadata_func=metadata_func
    )