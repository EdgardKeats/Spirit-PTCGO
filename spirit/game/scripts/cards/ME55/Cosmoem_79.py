from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7d148b4-6428-58e1-82a2-447be1db349a",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    display_name="Cosmoem",
    searchable_by=["Cosmoem", "Stage 1", "Cosmoem"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Stiffen",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=protect_next_turn(reduce=60),
        ),
    ],
)