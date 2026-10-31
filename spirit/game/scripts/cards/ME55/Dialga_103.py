from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card

card = PokemonCardDef(
    guid="1c799dc9-9f5a-57b1-af84-4eab2568a342",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Reversed Clock",
            game_text="Shuffle up to 3 in any combination of Pok\u00e9mon and Basic Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                predicate=(is_basic_energy_card or is_pokemon_card),
                count=3,
                to="deck_shuffle",
                prompt="Choose up to 3 Pok\u00e9mon or Basic Energy cards to shuffle into your deck.",
            ),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)