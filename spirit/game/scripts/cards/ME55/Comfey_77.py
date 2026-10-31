from spirit.game.card_effects.support_common import heal_targets
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3c04c05-175a-5f00-a656-f3c371febeba",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic", "Comfey"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Attack(
            title="Comforting Aroma",
            game_text="Heal 80 damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(80, "bench_choice"),
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)