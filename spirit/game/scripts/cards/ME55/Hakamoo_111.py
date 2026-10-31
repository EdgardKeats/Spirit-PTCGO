from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58c874c9-355d-520e-aaed-e4634f8bffbf",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    display_name="Hakamo-o",
    searchable_by=["Hakamo-o", "Stage 1", "Hakamoo"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
    ],
)