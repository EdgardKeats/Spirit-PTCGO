from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eee6d599-5ca5-506f-9499-ee890af3b11a",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    display_name="Cosmog",
    searchable_by=["Cosmog", "Basic", "Cosmog"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=789,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)