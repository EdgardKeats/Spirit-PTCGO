from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1972a25f-b6c2-50e2-ba4f-f5349490b718",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    display_name="Nidorina",
    searchable_by=["Nidorina", "Stage 1", "Nidorina"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Share Happiness",
            game_text="Once during your turn, you may use this Ability. Heal 30 damage from 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)