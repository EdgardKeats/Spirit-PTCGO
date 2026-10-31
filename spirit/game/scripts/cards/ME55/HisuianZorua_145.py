from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c99aa48-68a8-5a3f-876a-23b5e5d61692",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name",
    display_name="Hisuian Zorua",
    searchable_by=["Hisuian Zorua", "Basic", "HisuianZorua"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)